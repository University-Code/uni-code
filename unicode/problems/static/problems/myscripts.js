functionName= "playGround"

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


$(document).ready(()=>{
    
    //Initializes Editor
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");
    editor.setValue(boilierPlate['javascript'],0);

    //Changes Language based on selection
    $('select').change(()=>{
        option= languageSelection($('select').val());
        editor.session.setMode("ace/mode/"+option);
        console.log('yerr', option)
        editor.setValue(boilierPlate[option],0);
    
    })

    //Updates Text editor code 
    $("#editor").keyup(()=>{
       language= languageSelection($('select').val())
       boilierPlate[language]= editor.getValue()
       console.log(boilierPlate[language])
       //boilerPlate.getValue())
    })
        

     //Rotates arrow on menu drop down
    $(".account").click(()=>{
        $(".fa-chevron-down").toggleClass("rotate180")
    })

    // Shows/Hides User account menu
    $('.account').click(()=> {
        $('.user-menu').toggle()
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
   


