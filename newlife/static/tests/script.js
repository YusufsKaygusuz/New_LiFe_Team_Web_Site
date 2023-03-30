//selecting all required elements
const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const result_box = document.querySelector(".result_box");
const option_list = document.querySelector(".option_list");
const time_line = document.querySelector("header .time_line");
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");

// sınava Başla düğmesi tıklanırsa
start_btn.onclick = ()=>{
    info_box.classList.add("activeInfo"); //show info box
}

// sınavdan Çık düğmesi tıklanırsa
exit_btn.onclick = ()=>{
    info_box.classList.remove("activeInfo"); //sakla info box
}

// sınava devam Et düğmesi tıklanırsa
continue_btn.onclick = ()=>{
    info_box.classList.remove("activeInfo"); //sakla info box
    quiz_box.classList.add("activeQuiz"); //göster quiz box
    showQuetions(0); //showQestions fonksiyonunu çağır
    queCounter(1); // 1 parametre toque Sayacına ata
    startTimer(15); // startTimer fonksiyonunu çağırma
    startTimerLine(0); //startTimerLine fonksiyonunu çağırma
}

let timeValue =  15;
let que_count = 0;
let que_numb = 1;
let userScore = 0;
let counter;
let counterLine;
let widthValue = 0;

const restart_quiz = result_box.querySelector(".buttons .restart");
const quit_quiz = result_box.querySelector(".buttons .quit");

// sınavı Yeniden Başlat düğmesi tıklanırsa
restart_quiz.onclick = ()=>{
    quiz_box.classList.add("activeQuiz"); //göster quiz box
    result_box.classList.remove("activeResult"); //sakla result box
    timeValue = 15; 
    que_count = 0;
    que_numb = 1;
    userScore = 0;
    widthValue = 0;
    showQuetions(que_count); //showquestion fonksiyonunu çağırma
    queCounter(que_numb); // que_numb değerini quecounter'a geçirme
    clearInterval(counter); //süre sayacını temizle
    clearInterval(counterLine); //temizle counterLine
    startTimer(timeValue); //startTimer fonksiyonunu çağırma
    startTimerLine(widthValue); //startTimerLine fonksiyonunu çağırma
    timeText.textContent = "Kalan süre"; //timeText metnini Kalan Süre olarak değiştirin
    next_btn.classList.remove("show"); //sakla next button
}

// sınavdan Çık düğmesi tıklanırsa
quit_quiz.onclick = ()=>{
    window.location.reload(); //geçerli pencereyi yeniden yükle
}

const next_btn = document.querySelector("footer .next_btn");
const bottom_ques_counter = document.querySelector("footer .total_que");

// bir Sonraki Que düğmesi tıklanırsa
next_btn.onclick = ()=>{
    if(que_count < questions.length - 1){ //soru sayısı toplam soru uzunluğundan azsa
        que_count++; //que_count değerini artırın
        que_numb++; //que_numb değerini artırın
        showQuetions(que_count); //showquestion işlevini çağırma
        queCounter(que_numb); //que_numb değerini quecounter'a geçirme
        clearInterval(counter); //counter'ı temizle
        clearInterval(counterLine); //temizle counterLine
        startTimer(timeValue); //startTimer işlevini çağırma
        startTimerLine(widthValue); //startTimerLine işlevini çağırma
        timeText.textContent = "Kalan süre"; //zaman Metnini Kalan Süre olarak değiştirin
        next_btn.classList.remove("show"); //sakla next button
    }else{
        clearInterval(counter); //clear counter
        clearInterval(counterLine); //clear counterLine
        showResult(); //calling showResult function
    }
}

// diziden sorular ve seçenekler alma
function showQuetions(index){
    const que_text = document.querySelector(".que_text");

    // soru ve seçenek için yeni bir yayılma alanı ve div etiketi oluşturma ve dizi dizinini kullanarak değeri geçirme
    let que_tag = '<span>'+ questions[index].numb + ". " + questions[index].question +'</span>';
    let option_tag = '<div class="option"><span>'+ questions[index].options[0] +'</span></div>'
    + '<div class="option"><span>'+ questions[index].options[1] +'</span></div>'
    + '<div class="option"><span>'+ questions[index].options[2] +'</span></div>'
    + '<div class="option"><span>'+ questions[index].options[3] +'</span></div>';
    que_text.innerHTML = que_tag; //adding new span tag inside que_tag
    option_list.innerHTML = option_tag; //adding new div tag inside option_tag
    
    const option = option_list.querySelectorAll(".option");

    // onclick özelliğini kullanılabilir tüm seçeneklere ayarla
    for(i=0; i < option.length; i++){
        option[i].setAttribute("onclick", "optionSelected(this)");
    }
}
// simgeler için yeni div etiketleri oluşturma
let tickIconTag = '<div class="icon tick"><i class="fas fa-check"></i></div>';
let crossIconTag = '<div class="icon cross"><i class="fas fa-times"></i></div>';

// kullanıcı seçeneği tıkladıysa
function optionSelected(answer){
    clearInterval(counter); 
    clearInterval(counterLine);
    let userAns = answer.textContent;
    let correcAns = questions[que_count].answer;
    const allOptions = option_list.children.length;
    
    if(userAns == correcAns){ // kullanıcı tarafından seçilen seçenek dizinin doğru cevabına eşitse
        userScore += 1; // puan değerini 1 ile yükseltme
        answer.classList.add("correct"); // seçilen seçeneği düzeltmek için yeşil renk ekleme
        answer.insertAdjacentHTML("beforeend", tickIconTag); // seçilen seçeneği düzeltmek için onay simgesi ekleme
        console.log("Correct Answer");
        console.log("Your correct answers = " + userScore);
    }else{
        answer.classList.add("incorrect"); // seçili seçeneği düzeltmek için kırmızı renk ekleme
        answer.insertAdjacentHTML("beforeend", crossIconTag); // seçilen seçeneği düzeltmek için çarğı simgesi ekleme
        console.log("Wrong Answer");

        for(i=0; i < allOptions; i++){
            if(option_list.children[i].textContent == correcAns){ // bir dizi cevabıyla eşleşen bir seçenek varsa
                option_list.children[i].setAttribute("class", "option correct"); // eşleşen seçeneğe yeşil renk ekleme
                option_list.children[i].insertAdjacentHTML("beforeend", tickIconTag); // eşleşen seçeneğe tik simgesi ekleme
                console.log("Auto selected correct answer.");
            }
        }
    }
    for(i=0; i < allOptions; i++){
        option_list.children[i].classList.add("disabled"); // kullanıcı bir seçenek belirledikten sonra tüm seçenekleri devre dışı bıraktı
    }
    next_btn.classList.add("show"); // kullanıcı herhangi bir seçenek belirlediyse ileri düğmesini göster
}

function showResult(){
    info_box.classList.remove("activeInfo"); //sakla info box
    quiz_box.classList.remove("activeQuiz"); //sakla quiz box
    result_box.classList.add("activeResult"); //göster result box
    const scoreText = result_box.querySelector(".score_text");
    if (userScore > 7){ // kullanıcı 4'ten fazla puan aldıysa
        let scoreTag = '<span>Süper!😎 , Başarı oranın <p>'+ userScore +'</p> puan <p>'+ questions.length +'</p></span>';
        scoreText.innerHTML = scoreTag;  //adding new span tag inside score_Text
    }
    else if(userScore > 4){ // if user scored more than 3
        let scoreTag = '<span>Fena Değil!😊, Başarı oranın <p>'+ userScore +'</p> puan <p>'+ questions.length +'</p></span>';
        scoreText.innerHTML = scoreTag;
    }
    else{ // if user scored less than 1
        let scoreTag = '<span>Pek iyi değil!🤔 , Başarı oranın <p>'+ userScore +'</p> puan <p>'+ questions.length +'</p></span>';
        scoreText.innerHTML = scoreTag;
    }
}

function startTimer(time){
    counter = setInterval(timer, 1000);
    function timer(){
        timeCount.textContent = time; //changing the value of timeCount with time value
        time--; //decrement the time value
        if(time < 9){ // zamanlayıcı 9'dan küçükse
            let addZero = timeCount.textContent; 
            timeCount.textContent = "0" + addZero; // zaman değerinden önce 0 ekleyin
        }
        if(time < 0){ // zamanlayıcı 0'dan küçükse
            clearInterval(counter); //clear counter
            timeText.textContent = "Süre bitti"; //change the time text to süre bitti
            const allOptions = option_list.children.length; //getting all option items
            let correcAns = questions[que_count].answer; //getting correct answer from array
            for(i=0; i < allOptions; i++){
                if(option_list.children[i].textContent == correcAns){ //if there is an option which is matched to an array answer
                    option_list.children[i].setAttribute("class", "option correct"); //adding green color to matched option
                    option_list.children[i].insertAdjacentHTML("beforeend", tickIconTag); //adding tick icon to matched option
                    console.log("Time Off: Auto selected correct answer.");
                }
            }
            for(i=0; i < allOptions; i++){
                option_list.children[i].classList.add("disabled");
            }
            next_btn.classList.add("show");
        }
    }
}

function startTimerLine(time){
    counterLine = setInterval(timer, 29);
    function timer(){
        time += 1; //upgrading time value with 1
        time_line.style.width = time + "px"; //increasing width of time_line with px by time value
        if(time > 549){ //if time value is greater than 549
            clearInterval(counterLine); //clear counterLine
        }
    }
}

function queCounter(index){
    //Kullanıcının hangi soruda olduğunu gösteren barem
    let totalQueCounTag = '<span><p>'+ index +'</p>/<p>'+ questions.length +'</p> Sorudan</span>';
    bottom_ques_counter.innerHTML = totalQueCounTag;  //adding new span tag inside bottom_ques_counter
}