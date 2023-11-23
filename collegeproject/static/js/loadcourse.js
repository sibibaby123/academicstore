$(function(){
    $("#department").change(function(){
        data = {"dept_id": $(this).val()}
        $.get("/get-course/", data, function(resp){
            data = JSON.parse(resp)
            s = `<option value="--">--------------------</option>`
            for(var i=0; i<data.length;i++){
                s += `<option value="${data[i].id}">${data[i].name}</option>`
            }
            $("#course").html(s)
        })
    })
})
