import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { useTheme } from '@mui/material';

export default function PlayersInjuriesTable({ playerInjuries }) {
    console.log(playerInjuries)
    return (
        <Box sx={{height: 300}}>
            <TableContainer component={Paper} sx={{maxHeight: 300}}>
                <Table stickyHeader sx={{ width: '100%',   }} aria-label="sticky table">
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
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>Data</span>
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {playerInjuries?.data?.map((row) => (
                            <TableRow
                            key={row.game_id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 },   }}
                            >
                                <TableCell align="left">{row.game_id}</TableCell>
                                <TableCell align="left">{playerInjuries.translations[row.reason]}</TableCell>
                                <TableCell align="left">{(row.type == 'Missing Fixture') ? 'Não vai jogar' : 'Incerta'}</TableCell>
                                <TableCell align="left">{row.date}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}
