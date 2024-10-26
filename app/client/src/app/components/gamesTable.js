'use client'

import { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import Divider from '@mui/material/Divider';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { useTheme } from '@mui/material';

function createData(name, home, away, total, color) {
    const isDarkTheme = useTheme().palette.mode === 'dark';
    if(!isDarkTheme && color == '#fff') {
        color = '#000'
    }
    return { name, home, away, total, color };
}

function GamesTable({ teamsGamesInfo }) {
    const rows = [
        createData(
            'Vitórias', 
            teamsGamesInfo?.wins_home,
            teamsGamesInfo?.wins_away,
            teamsGamesInfo?.wins_total,
            '#32a852'
        ),
        createData(
            'Derrotas', 
            teamsGamesInfo?.losses_home,
            teamsGamesInfo?.losses_away,
            teamsGamesInfo?.losses_total,
            '#a83232'
        ),
        createData(
            'Empates', 
            teamsGamesInfo?.draws_home,
            teamsGamesInfo?.draws_away,
            teamsGamesInfo?.draws_total,
            '#a89c32'
        ),
        createData(
            'Total', 
            teamsGamesInfo?.games_played_home,
            teamsGamesInfo?.games_played_away,
            teamsGamesInfo?.games_played_total,
            '#fff'
        ),
    ];

    return (
        <Box sx={{height: 300}}>
            <p style={{paddingBottom: '10px', font: 'roboto'}}>Jogos</p>
            <Divider orientation="horizontal" style={{marginBottom: '15px'}} />
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 500 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>
                            </TableCell>
                            <TableCell align="right">
                                <span style={{fontWeight: 'bold'}}>Em casa</span>
                            </TableCell>
                            <TableCell align="right">
                                <span style={{fontWeight: 'bold'}}>Fora</span>
                            </TableCell>
                            <TableCell align="right">
                                <span style={{fontWeight: 'bold'}}>Total</span>
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                    {rows.map((row) => (
                        <TableRow
                        key={row.name}
                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                <span style={{fontWeight: 'bold', color: row.color}}>{row.name}</span>
                            </TableCell>
                            <TableCell align="right" style={{color: row.color}}>{row.home}</TableCell>
                            <TableCell align="right" style={{color: row.color}}>{row.away}</TableCell>
                            <TableCell align="right" style={{color: row.color}}>{row.total}</TableCell>
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}

export default GamesTable