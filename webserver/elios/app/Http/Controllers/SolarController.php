<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Solar;

class SolarController extends Controller
{
    public function index(Request $request)
    {
        $solar = Solar::all();

        return response()->json($solar);
    }

    public function store(Request $request)
    {
        $solar = Solar::create($request->all());

        return response()->json($solar);
    }

    public function update(Request $request, $id)
    {

        $solar = Solar::find($id);
        $solar->intensity = $request['intensity'];
        $solar->time = $request['time'];

        $solar->save();

        return "success updating solar";

    }

    public function show(Request $request, $id)
    {
        $solar = Solar::findOrFail($id);
        $solar->update($request->all());

        return response()->json($solar);
    }

    public function destroy(Request $request, $id)
    {
        Solar::find($id)->delete();

        return response()->json([],204);
    }
}
