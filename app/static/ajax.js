
$(document).ready(function() {
    $('#masv_no').focusout(function() {

        $.ajax({
            type : 'GET',
            url : '/tuition/'+$(this).val()
        })
        .done(function(data) {
            if (data.name == null) {
                alert('Không tìm thấy sinh viên')
            }
            $('.nameSvNo').text(data.name)
            if (data.hocphi == 'None') {
                alert('Sinh viên đã thanh toán đầy đủ học phí')
                $('.tienno').text(0)
            }else{
                $('.tienno').text(data.hocphi.tienno)
            }      
        })
    })
});