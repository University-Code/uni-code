     //Rotates arrow on menu drop down
    $(".account").click(()=>{
        $(".fa-chevron-down").toggleClass("rotate180")
    })

    // Shows/Hides User account menu
    $('.account').click(()=> {
        $('.user-menu').toggle()
    })

    
    function toggleUpvote(){
        let clicked = event.target;
        let value = clicked.getAttribute("value");
        let prob_id = clicked.getAttribute("prob_id"); 
        
        $.ajax(
            {
                type:"Get",
                url: "upvote/",
                data:{
                    prob_id: prob_id,
                    upvoted: value
                },
                success: function(data) 
                {
                    if(data == "not authenticated"){
                        alert("Must be logged in to 'like' problem.");
                        return
                    }
                        
                    console.log(data);
                    if(value === "true"){
                        clicked.setAttribute("value", "false");
                        clicked.classList.remove("upvote");
                        clicked.classList.add("upvoted");
                    } else {
                        clicked.setAttribute("value", "true");
                        clicked.classList.remove("upvoted");
                        clicked.classList.add("upvote");
                    }
                },
                
            });

    }


