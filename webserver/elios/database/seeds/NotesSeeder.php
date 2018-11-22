<?php

use Illuminate\Database\Seeder;
use App\Note;

class NotesSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Note::truncate();

	$faker = \Faker\Factory::create();

	for ($i = 0; $i < 200; $i++) {
	    Note::create([
		    'subject' => $faker->sentence(),
		    'body' => $faker->paragraph(),
		]);
        }
    }
}
