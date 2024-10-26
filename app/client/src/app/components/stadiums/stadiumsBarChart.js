'use client'

import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, LogarithmicScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { getCapacitiesData } from '../../api/stadium'; 

ChartJS.register(CategoryScale, LinearScale, LogarithmicScale, BarElement, Title, Tooltip, Legend);

const StadiumsBarChart = () => {
    const [chartData, setChartData] = useState({ labels: [], counts: [] });

    const dataBarStadium = {
        labels: chartData.labels,
        datasets: [
            {
                label: 'Ocorrências de estádios',
                data: chartData.counts,
                backgroundColor: 'rgba(75,192,192,1)',
            },
        ],
    };

    const optionsBarStadium = {
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

    useEffect(() => {
        const fetchData = async () => {
            const data = await getCapacitiesData()
            const labels = data?.map(item => item.interval);
            const counts = data?.map(item => item.count);
            setChartData({ labels, counts });
        };

        fetchData();
    }, []);

    return (
        <Bar data={dataBarStadium} options={optionsBarStadium} />
    );
};

export default StadiumsBarChart;