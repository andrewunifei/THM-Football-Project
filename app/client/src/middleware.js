// middleware.js
import { NextResponse } from 'next/server';

export function middleware(request) {
    const { searchParams } = request.nextUrl;
    if (!searchParams.has('code')) {
        return NextResponse.redirect(new URL('/teams', request.url));
    }
    return NextResponse.next();
}

export const config = {
    matcher: '/teams/explore',
};