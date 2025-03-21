document.addEventListener('DOMContentLoaded', () => {
    const bankSelect = document.getElementById('bank');
    const qrForm = document.getElementById('qr-form');
    const qrCodeContainer = document.getElementById('qr-code-container');
    const qrCodeDiv = document.getElementById('qr-code');
    const bankNameDisplay = document.getElementById('bank-name');
    const accountNumberDisplay = document.getElementById('account-number');
    const transferContentDisplay = document.getElementById('transfer-content');

    // Lấy danh sách ngân hàng từ API VietQR
    fetch('https://api.vietqr.io/v2/banks')
        .then(response => response.json())
        .then(data => {
            data.data.forEach(bank => {
                const option = document.createElement('option');
                option.value = bank.code;
                option.textContent = bank.name;
                bankSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Lỗi khi lấy danh sách ngân hàng:', error));

    // Tạo mã QR
    document.getElementById('generateQR').addEventListener('click', () => {
        const bankCode = bankSelect.value;
        const accountNumber = document.getElementById('accountNumber').value;
        const accountName = document.getElementById('accountName').value;
        const amount = document.getElementById('amount').value;
        const description = document.getElementById('description').value;

        if (!bankCode || !accountNumber || !amount || !description || !accountName) {
            alert('Vui lòng điền đầy đủ thông tin.');
            return;
        }

        const encodedDescription = encodeURIComponent(accountName + " - " + description);
        const qrCodeUrl = `https://img.vietqr.io/image/${bankCode}-${accountNumber}-compact.png?amount=${amount}&addInfo=${encodedDescription}&accountName=${accountName}`;

        qrCodeDiv.innerHTML = `<img src="${qrCodeUrl}" alt="Mã QR VietQR">`;
        bankNameDisplay.textContent = bankSelect.options[bankSelect.selectedIndex].text;
        accountNumberDisplay.textContent = accountNumber;
        transferContentDisplay.textContent = description;
        qrCodeContainer.style.display = 'block';
    });
});