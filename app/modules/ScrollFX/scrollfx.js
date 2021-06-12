navbar_height = 50 // Your navbar height in PX (just don't type px right...)
mavbar_lockClass = "toggled" // Lock navbar with this class
navbar_hoverTrigger = ".navbar" // Select wich element on your page can trigger the navbar by hover, it needs to be a .class or #id
navbar_target = ".navbar" // Your navbar .class or #id

var saved_scroll = 0; // Keep user scroll to compare it later

$(document).ready(function() {
    $(window).scroll(function() { // Exec when user scoll
          var new_scroll = $(window).scrollTop(); // Distance user scrolled from the top of the page
          if (new_scroll > saved_scroll){ // Compare if scrolled distance is higher (if it is then the navbar will be disabled)
              if ( new_scroll > 95){ // Be sure the user scrolled a bit before disabling navbar
                toggleNavbar("off");
                $(navbar_target).removeClass(navbar_lockClass);  
              } else { 
                  // pass
              }
            saved_scroll = new_scroll; // Gives saved scroll the new scroll value so we can use it later
          } else { // That's if new_scroll is lower than saved_scroll, meaning user has scrolled up so we enable the navbar
            toggleNavbar("on");
            $(navbar_target).addClass(navbar_lockClass);
            saved_scroll = new_scroll; // Gives saved scroll the new scroll value so we can use it later
          }
    });

    $(navbar_hoverTrigger).hover(function(){ // If user hover the navbar (as a litle bit of the navbar is still on the viewport)
      toggleNavbar("on"); // Activate navbar
    }, function(){ // When user stop hovering navbar
        if ($(navbar_target).hasClass(navbar_lockClass)){ // if the navbar is toggled, means the user is at top of page or has changed page then do nothing
            // pass
        } else { // if the navbar is not toggled just disable it
            toggleNavbar("off");
        }
    });
});

function toggleNavbar(status){
    if ( status == "on"){
      $(navbar_target).css("transform", "translateY(0px)");
    } else {
      $(navbar_target).css("transform", "translateY(-" + navbar_height + ")");
    } 
}