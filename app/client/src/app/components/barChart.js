'use client'

import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, LogarithmicScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { getCapacitiesData } from '../api/stadium'; 

ChartJS.register(CategoryScale, LinearScale, LogarithmicScale, BarElement, Title, Tooltip, Legend);

const BarChart = () => {
    const [chartData, setChartData] = useState({ labels: [], counts: [] });

    useEffect(() => {
        const fetchData = async () => {
            const data = await getCapacitiesData()
            const labels = data?.map(item => item.interval);
            const counts = data?.map(item => item.count);
            setChartData({ labels, counts });
        };

        fetchData();
    }, []);

    const data = {
        labels: chartData.labels,
        datasets: [
            {
                label: 'Ocorrências de estádios',
                data: chartData.counts,
                backgroundColor: 'rgba(75,192,192,1)',
            },
        ],
    };

    const options = {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Capacidade de pessoas',
                },
            },
            y: {
                type: 'logarithmic',
                title: {
                    display: true,
                    text: 'Ocorrências (Escala Log)',
                },
                ticks: {
                    callback: function(value) {
                        return Number(value).toLocaleString();
                    },
                },
            },
        }
    };

    return <Bar data={data} options={options} />;
};

export default BarChart;