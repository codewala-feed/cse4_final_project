const input_tag = document.getElementsByTagName("input")
const select_tag = document.getElementsByTagName("select")


function onShadow(common){
    for (let tag = 0; tag < common.length; tag++) {
        const element = common[tag];
        element.addEventListener("mouseenter", function(){
            element.style.boxShadow = "2px 2px 8px aliceblue";
            element.style.backgroundColor = "rgba(41, 39, 39, 0.2)";
        })
    
        element.addEventListener("mouseleave", function(){
            element.style.boxShadow = "";
            element.style.backgroundColor = "";

        })
    }
}
onShadow(input_tag)
onShadow(select_tag)