// components/BarChart.js

import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const SegmentBarChart = ({ data, data2 }) => {
    const labels = data ? Object.keys(data).sort((a, b) => {
        const rangeA = a.split('-').map(Number);
        const rangeB = b.split('-').map(Number);
        return rangeA[0] - rangeB[0];
    }) : '';

    const values = data ? labels.map(label => {
        return data[label].percentage ? parseFloat(data[label].percentage) : 0; // Keep as percentage
    }) : '';

    const totals = data ? labels.map(label => {
        return data[label].total || 0; // Get total values
    }) : '';

    const values2 = data2 ? labels.map(label => {
        return data2[label].percentage ? parseFloat(data2[label].percentage) : 0; // Keep as percentage
    }) : '';

    const totals2 = data2 ? labels.map(label => {
        return data2[label].total || 0; // Get total values
    }) : '';

    const chartData = {
        labels: labels,
        datasets: [
            {
                label: 'Gols realizados',
                data: values,
                backgroundColor: '#2572a8',
                borderColor: '#2572a8',
                borderWidth: 1,
                datalabels: {
                    anchor: 'end',
                    align: 'end',
                    formatter: (value, context) => {
                        const total = totals[context.dataIndex]; // Get corresponding total
                        return `${total}`; // Format as percentage and total
                    },
                },
            },
            {
                label: 'Gols tomados',
                data: values2,
                backgroundColor: '#a86425',
                borderColor: '#a86425',
                borderWidth: 1,
                datalabels: {
                    anchor: 'end',
                    align: 'end',
                    formatter: (value, context) => {
                        const total = totals2[context.dataIndex]; // Get corresponding total
                        return `${total}`; // Format as percentage and total
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
                max: 30,
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
                    text: 'Segmentos de tempo',
                },
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Distribuição de gols',
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

export default SegmentBarChart;