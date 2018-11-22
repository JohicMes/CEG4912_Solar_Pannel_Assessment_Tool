<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Note;

class NotesController extends Controller
{
    public function index(Request $request)
    {
        $notes = Note::all();

        return response()->json($notes);
    }

    public function store(Request $request)
    {
        $note = Note::create($request->all());

        return response()->json($note);
    }

    public function update(Request $request, $id)
    {

        $note = Note::find($id);
        $note->subject = $request['subject'];
        $note->body = $request['body'];

        $note->save();

        return "success updating note";

    }

    public function show(Request $request, $id)
    {
        $note = Note::findOrFail($id);
        $note->update($request->all());

        return response()->json($note);
    }

    public function destroy(Request $request, $id)
    {
        Note::find($id)->delete();

        return response()->json([],204);
    }
}
