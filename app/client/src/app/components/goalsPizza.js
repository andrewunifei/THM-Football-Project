// components/GoalsPieChart.js

import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

// Register necessary components with Chart.js
ChartJS.register(ArcElement, Tooltip, Legend);

const GoalsPieChart = ({ data }) => {
    const chartData = {
        labels: [
            'Goals For Home',
            'Goals For Away',
        ],
        datasets: [
            {
                label: 'Goals Analysis',
                data: [
                    data?.goals_for_home,
                    data?.goals_for_away,
                ],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)', // Goals For Home
                    'rgba(75, 192, 192, 1)',   // Goals For Away
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
                text: 'Goals For and Against Analysis',
            }
        }
    };

    return (
            <Pie data={chartData} options={options} />
    );
};

export default GoalsPieChart;
