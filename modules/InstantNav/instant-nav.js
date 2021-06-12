const templateFolder = "/templates/"; // Get local templates
var navLoadInstance; // Initialize navload instance so it can be cleared when changing page

$(document).ready(() => {
    $(document).on("click", ".pageChanger", function(){ // When user click on a pagechanger elt
            clearTimeout(navLoadInstance); // Clear navLoad instance
            var newPage = $(this).attr("page"); // get clicked elt destination
            var newTitle = $(this).attr("page-title");
            changePage(newPage, newTitle); // Change page to the desired page and give it a title
            $(".navbar").addClass("toggled"); // add toggled to navbar to be sure it is not affected by ScrollFx until user scrolls
    });

    navCheck(); // When document load, check the hash to see if a page needs to be loaded
});
function changePage(newPage, newTitle){
    console.log(newPage + " and " + newTitle);
    $(".pageChanger").removeClass("active"); // Remove all active classes for pageChangers
    if (newPage != "404") { // Only if newPage is not equal to 404
       document.title = newTitle; // Change document title to the new parsed one
    } else {
        document.title = "Error 404 - EncomPN"; // Give page a 404 title
    }
    $("html,body").animate({ scrollTop: 0 }, "swing", () => { // Rescroll up
        saved_scroll = 0; // Reset saved scroll so user doesn't get weird navbar
    });
    window.location.hash = newPage; // Change hash to the current page
};
function contentUnload(newPage){ 
    $(".content").addClass("cOff"); // Animation purpose
    navLoadInstance = setTimeout(() => { // Load instance so the content is unload and loaded
                            $(".page-content").empty();
                            loadContent(newPage);
                        },300);
};
function loadContent(newPage){
    $(".page-content").load( templateFolder + newPage + ".html" ); // load template on page
};

function navCheck(){
    clearTimeout(navLoadInstance); // Clear navLoad instance
    var newPage = window.location.hash; // get new hash
    var page = newPage.replace("#", ""); // parsing purpose 
    if (page == "") { // if hash is null
        changePage("home");
    } else { // if hash is unknow 
        alert("ERROR 404: The page you requested doesn't exist on this server. Please check URL. Redirecting to home page.")
        changePage("home");
    }
}


window.addEventListener('hashchange', function() { // Listen for hash changes
    navCheck();
}, false);





function toggleNavbar(status){
  if ( status == "on"){
    $(".navbar").css("transform", "translateY(0px)");
  } else {
    $(".navbar").css("transform", "translateY(-50px)");
  } 
}
function animateLoad(){ // Animation pupose
    setTimeout(() =>{ 
        $(".content").removeClass("cStand")
    },10)
}