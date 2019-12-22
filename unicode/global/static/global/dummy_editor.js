$(document).ready(()=>{   
    runOnce=false

    boilerPlate = `\nfor fizzbuzz in range(100):
    # number divisible by 3, print 'Fizz' 
    # in place of the number 
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue
  
    # number divisible by 5, print 'Buzz' 
    # in place of the number 
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    # number divisible by 15 (divisible
    # by both 3 & 5), print 'FizzBuzz' in 
    # place of the number 
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    # print numbers 
    print(fizzbuzz)`.split("");

    
    //Initializes Editor
    editor = ace.edit("dummy-editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.highlightActiveLine = false;
    editor.highlightSelectedWord = false;
    // updateEditor(boilerPlate);
    var counter = 0;
    var writtenText = "";

    
    setInterval(function(){
        if (counter < boilerPlate.length){
            writtenText += boilerPlate[counter];
            editor.setValue(writtenText);
            editor.clearSelection();
            counter++;
        }
        
    }, 70);

    
            
})
    

   
    
   
    