import Table from '@mui/material/Table';
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

export default function PlayersInjuriesTable({ teamsGamesInfo }) {
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
            '#3277a8'
        ),
    ];

    return (
        <Box sx={{height: 300}}>
            <TableContainer component={Paper}>
                <Table sx={{ width: '100%',   }} aria-label="sticky table">
                    <TableHead sx={{ backgroundColor: 'background.paper',   }}>
                        <TableRow>
                            <TableCell align="left">
                            <span style={{fontWeight: 'bold'}}>Código do Jogo</span>
                            </TableCell>
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>Tipo</span>
                            </TableCell>
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>Consequência</span>
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows.map((row) => (
                            <TableRow
                            key={row.name}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 },   }}
                            >
                                <TableCell align="left">Testing 1</TableCell>
                                <TableCell align="left">Testing 2</TableCell>
                                <TableCell align="left">Testing 3</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}
