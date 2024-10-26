'use client'

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { useTheme } from '@mui/material';

function createData(name, home, away, color) {
    const isDarkTheme = useTheme().palette.mode === 'dark';
    if(!isDarkTheme && color == '#fff') {
        color = '#000'
    }
    return { name, home, away, color };
}

export default function TeamsBiggestTable({ data }) {
    const rows = [
        createData(
            'Ganho', 
            data?.biggest_win_home,
            data?.biggest_win_away,
            '#32a852'
        ),
        createData(
            'Perdido', 
            data?.biggest_loss_home,
            data?.biggest_loss_away,
            '#a83232'
        )
    ];

    return (
        <Box>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 500 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>
                                <span>Maior jogo</span>
                            </TableCell>
                            <TableCell align="right">
                                <span style={{fontWeight: 'bold'}}>Em casa</span>
                            </TableCell>
                            <TableCell align="right">
                                <span style={{fontWeight: 'bold'}}>Fora</span>
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
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}
