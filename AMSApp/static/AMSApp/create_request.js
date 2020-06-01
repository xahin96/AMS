$(document).ready(function(){
    Init();
});

function Init() {
    $("#dvIPRequired").hide();
}

function IPRequired_Change() {
    if($('#id_form-ip_required').val() == "0"){
        $("#dvIPRequired").hide();
        $("#id_form_ip_information-ip_address").prop('required',false);
        $("#id_form_ip_information-port").prop('required',false);
    }
    else{
        $("#dvIPRequired").show();
        $("#id_form_ip_information-ip_address").prop('required',true);
        $("#id_form_ip_information-port").prop('required',true);
    }
}