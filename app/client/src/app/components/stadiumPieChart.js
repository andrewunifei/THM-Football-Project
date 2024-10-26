'use client'

import { useEffect, useState } from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title } from 'chart.js';
import { getSurfaceData } from '../api/stadium'; 
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(ArcElement, Title, Tooltip, Legend);

const resetChartRegistry = () => {
    ChartJS.unregister(ChartDataLabels);
};

const PieChart = () => {
    useEffect(() => {
        return () => {
            resetChartRegistry();
        };
    })

    const [data, setData] = useState({});

    const translations = {
        "artificial turf": "Fibra sintética",
        "grass": "Grama natural"
    };

    useEffect(() => {
        const fetchData = async () => {
            const data = await getSurfaceData();
            if(data){
                setData(data);
            }
        };

        fetchData();
    }, []);

    const chartData = {
        labels: Object.keys(data).map(label => translations[label] || label),
        datasets: [
            {
                label: 'Tipos de superfície',
                data: Object.values(data),
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(255, 99, 132, 0.6)',
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)',
                ],
                borderWidth: 1,
            },
        ],
    };

    const optionsStadium = {
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: 'Distribuição dos Tipos de Superfície',
                align: 'center',
                padding: {
                    top: 10,
                    bottom: 30,
                },
            },
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return (`${tooltipItem.label}: ${tooltipItem.raw}`);
                    },
                },
            },
        },
    };

    return (
        <Pie data={chartData} options={optionsStadium} />
    );
};

export default PieChart;