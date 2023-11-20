<?php

namespace App\Models;
use App\models\User;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class clientes extends Model
{
    use HasFactory;
    protected $fillable = [
        'nombre',
        'apellido',
        'correo',
        'telefono',
        'nro_doc',
    ];
    public function users()
    {
        return $this->belongsTo(User::class, 'id_cliente', 'id');
    }
}
