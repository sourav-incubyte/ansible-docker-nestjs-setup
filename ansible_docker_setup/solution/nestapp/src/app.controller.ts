import { Controller, Get } from '@nestjs/common';
import { Pool } from 'pg';

const pool = new Pool({
  host: 'postgres',
  port: 5432,
  user: 'admin',
  password: 'secret',
  database: 'appdb',
});

@Controller()
export class AppController {
  @Get('/checkdb')
  async checkDatabase() {
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