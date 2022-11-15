
$(document).ready(function() {
    $('#masv_dept').focusout(function() {
        
        $.ajax({
            type : 'GET',
            url : '/tuition/'+$(this).val()
        })
        .done(function(data) {
            if (data.error){
                alert(data.error)
            }
            else{
                if (data.name == null) {
                    alert('Không tìm thấy sinh viên')
                }else{
                    $('#namesv_dept').val(data.name)
                    $('#namesv_dept').prop('disabled', true);
                }
                if (data.hocphi == 'None') {
                    alert('Sinh viên đã thanh toán đầy đủ học phí')
                    $('.sotienno').val("0")
                }else{
                    $('#sotienno').val(data.hocphi)
                    $('#sotienno').prop('disabled', true);
                    $('#sotien').val(data.hocphi)
                    $('#sotien').prop('disabled', true);
                    $('#hidden').val(data.id)
                   
                }
            }
           
        })
    })

    
});