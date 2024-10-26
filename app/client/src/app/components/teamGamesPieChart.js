'use client'

import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(ArcElement, Title, Tooltip, Legend, ChartDataLabels);

const TeamGamesPieChart = ({ teamsGamesInfo }) => {
    React.useEffect(() => {
        ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);
    }, [])

    const data = {
        labels: ['Vitórias', 'Derrotas', 'Empates'],
        datasets: [{
            label: 'Total',
            data: [
                teamsGamesInfo?.wins_total,
                teamsGamesInfo?.losses_total,
                teamsGamesInfo?.draws_total,
            ],
            backgroundColor: [
                '#32a852', // Cor da vitória
                '#a83232', // Cor da derrota
                '#a89c32' // Cor do empate
            ],
            borderColor: [
                '#000', // Cor da vitória
                '#000', // Cor da derrota
                '#000' // Cor do empate
            ],
            borderWidth: 1,
        }],
    };

    const optionsTeams = {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Resultados dos jogos'
            },
            tooltip: {
                callbacks: {
                    label: function (tooltipItem) {
                        const label = tooltipItem.label || '';
                        const value = tooltipItem.raw || 0;
                        const total = tooltipItem.chart.data.datasets[0].data.reduce((a, b) => a + b);
                        const percentage = ((value / total) * 100).toFixed(2) + '%'; // Calculate percentage
                        return (`${label}: ${value} (${percentage})`); 
                    }
                }
            },
            datalabels: {
                color: '#fff',
                formatter: (value, context) => {
                    const total = context.chart.data.datasets[0].data.reduce((a, b) => a + b);
                    const percentage = ((value / total) * 100).toFixed(2) + '%';
                    return percentage; // Show percentage on each section
                },
            }
        }
    };

    return (
        <Pie data={data} options={optionsTeams} />
    );
};

export default TeamGamesPieChart;