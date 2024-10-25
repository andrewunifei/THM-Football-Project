'use client'

import { useState, useEffect } from 'react';
import { useSearchParams } from 'next/navigation'
import Box from '@mui/material/Box';
import { PageContainer, PageContainerToolbar } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import Divider from '@mui/material/Divider';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { usePathname } from 'next/navigation';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItemText from '@mui/material/ListItemText';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';

function PageToolbar() {
    return (
        <p>hello</p>
    );
  }

function getTitle(logo, name) {
    return (
        <List sx={{ width: '100%', display: 'flex', alignItems:"flex-start" }}>
            <ListItem>
                <ListItemAvatar>
                    <Avatar alt="logo" src={logo}/>
                </ListItemAvatar>
                {name}
            </ListItem>
        </List>
    )
}

function ExploreTeam() {
    const searchParams = useSearchParams();
    const code = searchParams.get('code')
    const name = searchParams.get('name')
    const logo = searchParams.get('logo')

    function createData(name, calories, fat, carbs, protein) {
        return { name, calories, fat, carbs, protein };
    }
      
      const rows = [
        createData('Vitórias', 159, 6.0, 24, 4.0),
        createData('Derrotas', 237, 9.0, 37, 4.3),
        createData('Empates', 262, 16.0, 24, 6.0),
        createData('Total', 305, 3.7, 67, 4.3),
    ];

    function getBread() {
        return [
            {
                path: '/teams',
                title: 'Times'
            },
            {
                path: '',
                title: 'Explorar'
            }
        ]
    }

    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
        <PageContainer maxWidth="xl" slots={{toolbar: PageToolbar}} breadcrumbs={getBread()} title={getTitle(logo, name)}>
          <Grid container spacing={3} >
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
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
                                                    {row.name}
                                                </TableCell>
                                                <TableCell align="right">{row.calories}</TableCell>
                                                <TableCell align="right">{row.fat}</TableCell>
                                                <TableCell align="right">{row.carbs}</TableCell>
                                                </TableRow>
                                            ))}
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                            </Box>
                        </Paper>
                    </Grid>
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                        <Box sx={{height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>

                        </Box>
                        </Paper>
                    </Grid>
                </Grid>
        </PageContainer>
      </Paper>
    )
}

export default ExploreTeam;