function submitForm_filter_platform(){
    //获取form表单对象,提交选择项目
    var form = document.getElementById("add_group");
    form.submit();//form表单提交
}
function stopBubble(e){

　　if(e&&e.stopPropagation){//非IE

　　　　e.stopPropagation();

　　}else{//IE

　　　　window.event.cancelBubble=true;

　　}

}
