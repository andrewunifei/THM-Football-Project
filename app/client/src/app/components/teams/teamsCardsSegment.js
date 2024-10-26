import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default  function TeamsCardsSegment({ data, cards_color, bar_color, label }) {
    const labels = data ? Object.keys(data).sort((a, b) => {
        const rangeA = a.split('-').map(Number);
        const rangeB = b.split('-').map(Number);
        return rangeA[0] - rangeB[0];
    }) : '';

    const values = data ? labels.map(label => {
        return data[label].percentage ? parseFloat(data[label].percentage) : 0;
    }) : '';

    const totals = data ? labels.map(label => {
        return data[label].total || 0;
    }) : '';

    const chartData = {
        labels: labels,
        datasets: [
            {
                label,
                data: values,
                backgroundColor: bar_color,
                borderColor: bar_color,
                borderWidth: 1,
                datalabels: {
                    anchor: 'end',
                    align: 'end',
                    formatter: (value, context) => {
                        const total = totals[context.dataIndex];
                        return `${total}`;
                    },
                },
            }
        ]
    };

    const options = {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                min: 0,
                max: cards_color == 'vermelhos' ? 100 : 50,
                title: {
                    display: true,
                    text: 'Porcentagem (%)'
                },
                ticks: {
                    callback: (value) => `${value}%`,
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Segmentos de tempo dos jogos',
                },
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: `Distribuição de cartões ${cards_color}`,
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        const value = tooltipItem.raw;
                        return `${value}%`; 
                    }
                }
            }
        }
    };

    return (
        <Bar data={chartData} options={options} plugins={[ChartDataLabels]} />
    );
};
