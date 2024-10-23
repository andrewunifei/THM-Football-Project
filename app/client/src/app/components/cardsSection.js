import * as React from 'react';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import MediaCard from './mediaCard';
import Box from '@mui/material/Box';

export default function CardsSection({ title }) {
    return (
        <>
            <h2 style={{paddingBottom: '10px', font: 'roboto'}}>{title}</h2>
            <Grid container spacing={1}>
            <Grid size={4}>
                <Box>
                <MediaCard/>
                </Box>
            </Grid>
            <Grid size={4}>
                <Box>
                <MediaCard/>
                </Box>
            </Grid>
            <Grid size={4}>
                <Box>
                <MediaCard/>
                </Box>
            </Grid>
            </Grid>
        </>
    )
}