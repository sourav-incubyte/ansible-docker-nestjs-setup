import { Controller, Get } from '@nestjs/common';
import { Pool } from 'pg';

const pool = new Pool({
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT),
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

@Controller()
export class AppController {

  @Get('/healthz')
  async checkDb() {
    try {
      const client = await pool.connect();
      await client.query('SELECT 1');
      client.release();
      return { status: 'ok' };
    } catch (err) {
      return { status: 'error', message: err.message };
    }
  }
}