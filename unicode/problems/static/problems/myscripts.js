
$(document).ready(()=>{
    // var code= $(".codemirror-textarea")[0];
    // options= {
    //     lineNumbers: true,
    //     keyMap: "sublime",
    //     lineNumbers: true,
    //     mode: "javascript",
    //    autoCloseBrackets: true,
    //     matchBrackets: true,
    //     showCursorWhenSelecting: true,
    //     theme: "monokai",
    //     tabSize: 2

    // }
    // var editor= CodeMirror.fromTextArea(code, options)

    

    //Initializes Editor
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");

    //Changes Language based on selection
    $('select').change(()=>{
        option= languageSelection($('select').val());
        editor.session.setMode("ace/mode/"+option);

        console.log(option)
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
   


