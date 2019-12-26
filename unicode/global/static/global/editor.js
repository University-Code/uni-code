$(document).ready(()=>{ 
    difficultyColor()
    formatDescription()

    let language= $( ".select-language" ).val();
    let problemTitle= $('#problem_title').html()
    let boilerPlate= boilerPlateCode(problemTitle);
        

    //Initializes Editor
    const editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");
    editor.setValue(boilerPlate['javascript'],0);

    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true,
     });
    //Changes Language based on selection
    $('.select-language').change(()=>{
        language= $('.select-language').val()
        option= languageSelection($('.select-language').val());
        editor.session.setMode("ace/mode/"+option);        
        editor.setValue(boilerPlate[option],0);
    })

    //Chages Theme of Editor
    $('.select-theme').change(()=>{
        theme= $('.select-theme').val().toLowerCase()
        console.log(theme)
        editor.setTheme("ace/theme/"+theme)

        //Close window
        $(".close").trigger('click')
    })

    //Updates Text editor code 
    $("#editor").keyup(()=>{
        language= languageSelection($('.select-language').val())
        boilerPlate[language]= editor.getValue()
        console.log(boilerPlate[language])
    })

    //Code submission
    $("#user_submission").submit((e)=>{    
        e.preventDefault()
        userSubmission(editor)
    })
})
    
 


//***********************//
//******* FUNCTIONS******//
//***********************//

//Converts Language to Ace Editor Format
function languageSelection(option){
    option= option.toLowerCase()
    var select='javascript';

    switch(option){
        case "c++":
            select= 'c_cpp'
            break;
        case "c#":
            select="csharp"
            break;
        case "python":
            select='python'
            break;
        case "java":
            select='java'
            break;
        case "clojure":
            select='clojure'
            break;
        default:
            select=option
            break;
    }

    return select
}

//Changes color of question difficulty text
function difficultyColor(){
    console.log('hello')
    difficulty= $('.difficulty').html().toLowerCase()

    switch(difficulty){
        case "easy":
            $('.difficulty').css("color", "green")
            break;

        case "medium":
            $('.difficulty').css("color","rgb(255, 174, 0)")
            break;

        case "hard":
            $('.difficulty').css("color", 'red');
            break;
    }
}

function boilerPlateCode(functionName){
    //Boiler Plate Code for autoloading code
    boilerPlate={
        //JavaScript
        "javascript":`function ${titleToFunctionName(functionName,"JavaScript")}(word){
                \r}`,
        
        //Java
        "java":`class Program{\r\tpublic static void main (String[]args){
                        \r\t\tString ${titleToFunctionName(functionName,"Java")}(String word){
                            \r\t\t\tSystem.out.println("Hello World!")
                            \r\t\t}\r\t}\r}`,
        
        //Python
        "python": `def ${titleToFunctionName(functionName,"Python")}(word):`,

        //C#
        "csharp": 
        
                `public class Program{\r\tpublic static void ${titleToFunctionName(functionName,"C#")}(){
                    \r\t\tConsole.WriteLine("Hello World!");
                    \r\t}
            \r}`,

        //C++       
        "c_cpp": 
                `#include <iostream>\nusing namespace std;\nint ${titleToFunctionName(functionName,"C++")}(){
                    \r\tcout << "Hello World" << endl;\r\treturn 0;
                \r}`,
        //Clojure
        "clojure": "IDK"

    }

    return boilerPlate;

}

function convert_to_single_line(code) {
    // the lesson here is to NEVER TARGET IE WITHOUT JQUERY
    if (window.is_ie_lt9) {
        code = code.replace(/(\r\n|\r|\n)/g, '\n');
    }
    var ix;
    var lines = code.trimRight() // keep left indent
                    .replace(/\\/g, '\\\\') //  escape all \
                    .replace(/"""/g, '\\"\\"\\"') // escape """
                    .split('\n');
    var first_indent;
    for (ix = 0; ix < lines.length; ++ix) {
        if (first_indent === undefined) {
            first_indent = lines[ix].match(/^\s*/);
        }
        if (true) {
            lines[ix] = lines[ix].replace(new RegExp('^'+first_indent), '');
        }
    }
    // lines.unshift('"');
    // lines.push('"');
		return lines.join('\\n')
}



function userSubmission(editor){

    //Collects data for Judge API
    var codingLanguage= $('.select-language').val()
    
    var userCode=editor.getValue() 
    
    if(codingLanguage=='Python')
        userCode= convert_to_single_line(userCode)
    console.log(userCode)
    $.ajax({
        type: 'post',
        url: '', //Same page
        data: {
            language: codingLanguage,
            code: userCode,
            csrfmiddlewaretoken: window.CSRF_TOKEN
        },
        dataType: 'json',
        success: function (response) {
            $('.confetti').show()
            displayConsoleOutput(response)
            confettiDropdown()
            setTimeout(()=>{$('.confetti').hide()},5000)
           

        }
    });
}

//Converts TItle Name to Function Name based on language
function titleToFunctionName(string,language){
    let functionName=''
    if(language=="Python"){
        //Under score format
        string=string.toLowerCase()
        functionName= string.split(" ").join("_")
    }
    else{
        //Camel case format
        string= string.split(" ").map(x=> x.charAt(0).toUpperCase() + x.slice(1)).join("")
        functionName= string.charAt(0).toLowerCase() +string.slice(1)
    }
    return functionName
}

    
//Enable Tool Tip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

function formatDescription(){

   //Get description -> replace escape strings with empty character -> trim whitespace
   let description= $('.description div').first().html().replace(/(\r\n|\n|\r)/gm, "").trim();

   //Breaks up description into list by every other period
   let descriptionList=description.match(/[^.]+.[^.]+/g);

   //Displays description in html
   descriptionList.forEach(element => {
       $('.description').append(`<div class='description-sentence'> ${element} </div>`)
   });

   //Delete original description
   $('.description div').first().empty()
}

function displayConsoleOutput(response){
                //Clears Ouput and listed Test Cases from Console
                $('.test-cases').empty()
                $('#console').removeClass('collapse')
                $('.output').empty()
    
                if(response.error){
                    $('.output').append(`<code> ${response.error} </code>`)
                    return
                }
                else{
                    console.log('yahh you passed')
                    let percentage=0
                    total=0
                    //Loops through test cases and displays them based on pass/fail
                    Object.keys(response).forEach(key => {
                        let testCaseInput= response[key].test_input
                        let testCaseOutput= response[key].test_output
                        response[key].status=='pass'? status='fas fa-check': status='fas fa-times'

                        if(response[key].status== 'pass')
                            percentage++                        
                        $('.test-cases').append(`<div>
                                                    <code> 
                                                        <span style='color:black'>Input</span>
                                                        ${testCaseInput} 
                                                        <i class="fas fa-angle-double-right" style='color:black'></i>
                                                        <span style='color:black'> Output </span>
                                                        ${testCaseOutput}
                                                    </code>
                                                    
                                                    <span> <i class='${status}'></i> </span>`)
                        total++;
                    })
                    const consoleOutput= `Your soloution is + ${(percentage/total)*100}% correct!`
                    console.log(consoleOutput)

                    $('.output').append(consoleOutput)

                }

}

function confettiDropdown(){
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    cx = ctx.canvas.width/2;
    cy = ctx.canvas.height/2;

    let confetti = [];
    const confettiCount = 300;
    const gravity = 0.5;
    const terminalVelocity = 5;
    const drag = 0.075;
    const colors = [
    { front : 'red', back: 'darkred'},
    { front : 'green', back: 'darkgreen'},
    { front : 'blue', back: 'darkblue'},
    { front : 'yellow', back: 'darkyellow'},
    { front : 'orange', back: 'darkorange'},
    { front : 'pink', back: 'darkpink'},
    { front : 'purple', back: 'darkpurple'},
    { front : 'turquoise', back: 'darkturquoise'},
    ];

    //-----------Functions--------------
    resizeCanvas = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        cx = ctx.canvas.width/2;
        cy = ctx.canvas.height/2;
    }

    randomRange = (min, max) => Math.random() * (max - min) + min

    initConfetti = () => {
    for (let i = 0; i < confettiCount; i++) {
        confetti.push({
        color      : colors[Math.floor(randomRange(0, colors.length))],
        dimensions : {
            x: randomRange(10, 20),
            y: randomRange(10, 30),
        },
        position   : {
            x: randomRange(0, canvas.width),
            y: canvas.height - 1,
        },
        rotation   : randomRange(0, 2 * Math.PI),
        scale      : {
            x: 1,
            y: 1,
        },
        velocity   : {
            x: randomRange(-25, 25),
            y: randomRange(0, -35),
        },
        });
    }
    }

    //---------Render-----------
    render = () => {  
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    confetti.forEach((confetto, index) => {
        let width = (confetto.dimensions.x * confetto.scale.x);
        let height = (confetto.dimensions.y * confetto.scale.y);
        
        // Move canvas to position and rotate
        ctx.translate(confetto.position.x, confetto.position.y);
        ctx.rotate(confetto.rotation);
        
        // Apply forces to velocity
        confetto.velocity.x -= confetto.velocity.x * drag;
        confetto.velocity.y = Math.min(confetto.velocity.y + gravity, terminalVelocity);
        confetto.velocity.x += Math.random() > 0.5 ? Math.random() : -Math.random();
        
        // Set position
        confetto.position.x += confetto.velocity.x;
        confetto.position.y += confetto.velocity.y;
        
        // Delete confetti when out of frame
        if (confetto.position.y >= canvas.height) confetti.splice(index, 1);

        // Loop confetto x position
        if (confetto.position.x > canvas.width) confetto.position.x = 0;
        if (confetto.position.x < 0) confetto.position.x = canvas.width;

        // Spin confetto by scaling y
        confetto.scale.y = Math.cos(confetto.position.y * 0.1);
        ctx.fillStyle = confetto.scale.y > 0 ? confetto.color.front : confetto.color.back;
        
        // Draw confetto
        ctx.fillRect(-width / 2, -height / 2, width, height);
        
        // Reset transform matrix
        ctx.setTransform(1, 0, 0, 1, 0, 0);
    });

    // Fire off another round of confetti
    // if (confetti.length <= 10) initConfetti();

    window.requestAnimationFrame(render);
    }

    //---------Execution--------
    initConfetti();
    render();


    //----------Resize----------
    // window.addEventListener('resize', function () {
    // resizeCanvas();
    // });
  
}

