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
            displayConsoleOutput(response)
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
                    console.log(percentage)
                    console.log(`Your soloution is + ${(percentage/total)*100}% correct!`)
                }

}

