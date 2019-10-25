$(document).ready(()=>{

functionName= $('#function_name').html()
boilierPlate= boilerPlateCode();
var editor = ace.edit("editor");

difficultyColor();

$("#user_submission").submit((e)=>{    
    e.preventDefault()
    userSubmission(editor)

})



    //Initializes Editor
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");
    editor.setValue(boilierPlate['javascript'],0);

    //Changes Language based on selection
    $('.select-language').change(()=>{
        option= languageSelection($('.select-language').val());
        editor.session.setMode("ace/mode/"+option);
        console.log('yerr', option)
        editor.setValue(boilierPlate[option],0);
    
    })

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
       boilierPlate[language]= editor.getValue()
       console.log(boilierPlate[language])
    })
        


})


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

function boilerPlateCode(){
    //Boiler Plate Code for autoloading code
    boilierPlate={
        //JavaScript
        "javascript":`function ${functionName}(word){
                \r}`,
        
        //Java
        "java":`class Program{\r\tpublic static void main (String[]args){
                        \r\t\tString ${functionName}(String word){
                            \r\t\t\tSystem.out.println("Hello World!")
                            \r\t\t}\r\t}\r}`,
        
        //Python
        "python": `def ${functionName}(word):`,

        //C#
        "csharp": 
        
                `public class Program{\r\tpublic static void ${functionName}(){
                    \r\t\tConsole.WriteLine("Hello World!");
                    \r\t}
            \r}`,

        //C++       
        "c_cpp": 
                `#include <iostream>\nusing namespace std;\nint ${functionName}(){
                    \r\tcout << "Hello World" << endl;\r\treturn 0;
                \r}`,
        //Clojure
        "clojure": "IDK"

    }

    return boilierPlate;

}

function userSubmission(editor){

    //Collects data for Judge API
    var codingLanguage= $('.language').val()
    var userCode=editor.getValue() 
        
    $.ajax({
    type: 'post',
    url: 'test/',
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

   
//Enable Tool Tip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

