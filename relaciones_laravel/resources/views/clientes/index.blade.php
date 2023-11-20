@extends('layouts.app')

@section('content')
<a href="{{ route('clientes.create') }}">Create new client</a>
@forelse ($cliente as $clientes)
    <li>
        <p>{{ $clientes->nombre }} -- {{ $clientes->apellido }} -- {{ $clientes->correo }} -- {{ $clientes->telefono }} -- {{ $clientes->nro_doc }} -- {{ $clientes->users ? $clientes->users->nombre_usuario : 'sin nada' }}</p>
    </li>
@empty
    <h6>No hay datos</h6>
@endforelse
@endsection