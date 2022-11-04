
$(document).ready(function() {
    $('#masv_no').focusout(function() {
        console.log('Ajax is working');
        console.log($('#masv-no').val());
        $.ajax({
            type : 'GET',
            url : '/tuition/'+$('#masv-no').val()
        })
        .done(function(data) {
            if (data.name == null) {
                alert('Không tìm thấy sinh viên')
            }
            if (data.tienno == null) {
                alert('Sinh viên đã thanh toán đầy đủ học phí')
            }
            $('#name').val(data.name);
            $('#tienno').val(data.tienno)
        })
    })
});