// components/GoalsPieChart.js

import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(ArcElement, Tooltip, Legend);

export default function TeamsGoalsPieChart({ for_data, against_data, name }) {
    const chartData = {
        labels: [
            'Gols realizados',
            'Gols tomados'
        ],
        datasets: [
            {
                data: [
                    for_data,
                    against_data,
                ],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(75, 192, 192, 1)', 
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(75, 192, 192, 1)',
                ],
                borderWidth: 1,
            }
        ]
    };

    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: name,
            },
            datalabels: {
                color: '#fff',
                formatter: (value, context) => {
                    const total = context.chart.data.datasets[0].data.reduce((a, b) => a + b);
                    const percentage = ((value / total) * 100).toFixed(2) + '%';
                    return percentage;
                },
            }
        }
    };

    return (
            <Pie data={chartData} options={options} plugins={[ChartDataLabels]} />
    );
};
