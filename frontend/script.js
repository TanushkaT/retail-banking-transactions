async function loadDashboard() {
    try {
        // Replace with your local FastAPI URL
        const response = await fetch('http://127.0.0.1');
        const data = await response.json();

        // 1. Update Metric Cards
        document.getElementById('total-txns').innerText = data.totals.total_txns;
        document.getElementById('total-volume').innerText = `$${data.totals.total_volume.toFixed(2)}`;

        // 2. Prepare Chart Data
        const labels = data.top_merchants.map(m => m.name); // merchant name
        const values = data.top_merchants.map(m => m.amount); // spent amount

        // 3. Render Chart
        const ctx = document.getElementById('merchantChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Spend per Merchant ($)',
                    data: values,
                    backgroundColor: '#4e73df'
                }]
            }
        });
    } catch (error) {
        console.error("Error loading dashboard:", error);
    }
}

loadDashboard();
