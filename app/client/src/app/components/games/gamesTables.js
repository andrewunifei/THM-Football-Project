import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import { useTheme } from '@mui/material';

export default function GamesTable({ games }) {
    return (
        <Box sx={{height: 300}}>
            <TableContainer component={Paper} sx={{maxHeight: 300}}>
                <Table stickyHeader sx={{ width: '100%'}} aria-label="sticky table">
                    <TableHead sx={{ backgroundColor: 'background.paper',   }}>
                        <TableRow>
                            <TableCell align="left">
                            <span style={{fontWeight: 'bold'}}>Código do Jogo</span>
                            </TableCell>
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>{'Casa'}</span>
                            </TableCell>
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>{'Fora'}</span>
                            </TableCell>
                            <TableCell align="left">
                                <span style={{fontWeight: 'bold'}}>{'Data'}</span>
                            </TableCell>
                            <TableCell align="left">
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {games?.map((item, index) => (
                            <TableRow
                            key={item.game_id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 },   }}
                            >
                                <TableCell align="left">{item.game_id}</TableCell>
                                <TableCell align="left">{'Arsenal'}</TableCell>
                                <TableCell align="left">{'Manchester United'}</TableCell>
                                <TableCell align="left">{item.date}</TableCell>
                                <TableCell>
                                    <Button variant="contained">Explorar</Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}
