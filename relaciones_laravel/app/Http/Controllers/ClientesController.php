<?php

namespace App\Http\Controllers;
use App\models\clientes;

use Illuminate\Http\Request;

class ClientesController extends Controller
{
    public function index(){
        // $cliente = clientes::all();
        // return view('clientes.index', ['cliente'=>$cliente]);
        $clientes = clientes::with('users')->get();
        return view('clientes.index', ['cliente' => $clientes]);
    }

    public function create()
    {
        return view("clientes.create");
    }


    public function store(Request $request)
    {

        clientes::create($request->all());
        
        $cliente = clientes::with('users')->get();

        return redirect()->route("clientes.index")->with("success","clientes registrado exitosamente");
        
    }
    
}
