$(document).ready(()=>{   
    runOnce=false

    //underScoreToCamelCase()    
    language= $( ".select-language" ).val();
    problemTitle= $('#problem_title').html()

    // console.log(problemTitle)
    boilerPlate= boilerPlateCode(problemTitle);
    
    difficultyColor();
    
    $("#user_submission").submit((e)=>{    
        e.preventDefault()
        userSubmission(editor)
    })
    
    
    
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

    function titleToFunctionName(string,language){
        if(language=="Python"){
            string=string.toLowerCase()
            functionName= string.split(" ").join("_")
        }
        else{
            string= string.split(" ").map(x=> x.charAt(0).toUpperCase() + x.slice(1)).join("")
            functionName= string.charAt(0).toLowerCase() +string.slice(1)

        }
        
        console.log(functionName)
        return functionName
    }

       
    //Enable Tool Tip
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })
    
    