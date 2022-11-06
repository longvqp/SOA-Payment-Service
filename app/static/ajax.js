
$(document).ready(function() {
    $('#masv_dept').focusout(function() {

        $.ajax({
            type : 'GET',
            url : '/tuition/'+$(this).val()
        })
        .done(function(data) {

            if (data.name == null) {
                alert('Không tìm thấy sinh viên')
            }
            $('#namesv_dept').val(data.name)
            $('#namesv_dept').prop('disabled', true);
            if (data.hocphi == 'None') {
                alert('Sinh viên đã thanh toán đầy đủ học phí')
                $('.sotienno').val("0")
            }
            $('#sotienno').val(data.hocphi)
            $('#sotienno').prop('disabled', true);
            $('#sotien').val(data.hocphi)
            $('#sotien').prop('disabled', true);
            $('#hidden').val(data.id)
        })
    })
});