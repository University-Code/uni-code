$(document).ready(()=>{ 
    //Changes color for difficulty  
    difficultyColor()
    formatDescription()

    language= $( ".select-language" ).val();
    problemTitle= $('#problem_title').html()
    boilerPlate= boilerPlateCode(problemTitle);
        

    //Initializes Editor
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");
    editor.setValue(boilerPlate['javascript'],0);

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
        default:
            select=option
            break;
    }

    return select
}

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

function userSubmission(editor){

    //Collects data for Judge API
    var codingLanguage= $('.language').val()
    var userCode=editor.getValue() 
        
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
        console.log(response)
        input= response.submission
        console.log(input)
    }
    });
}

//Converts TItle Name to Function Name based on language
function titleToFunctionName(string,language){
    if(language=="Python"){
        string=string.toLowerCase()
        functionName= string.split(" ").join("_")
    }
    else{
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
   var description= $('.description div').first().html().replace(/(\r\n|\n|\r)/gm, "").trim();

   //Breaks up description into list by every other period
   descriptionList=description.match(/[^.]+.[^.]+/g);

   descriptionList.forEach(element => {
       $('.description').append(`<div class='description-sentence'> ${element} </div>`)
   });

   //Delete original description
   $('.description div').first().empty()
}

