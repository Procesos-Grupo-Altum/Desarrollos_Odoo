for record in self: 
# -------------------------------------------------
# Inicialización segura
# -------------------------------------------------
    lineasBiEmple = []

# -------------------------------------------------
# Resolver modelo destino
# -------------------------------------------------
    modelo = self.env['ir.model'].search(
        [('model', '=', record.res_model)],
        limit=1)

    if not modelo:
        record['x_documentos_ids'] = [(5, 0, 0)]
        continue

    model_id = modelo.id
    TargetModel = self.env[record.res_model]

# -------------------------------------------------
# 1) Resolver campo adjunto dinámico
# -------------------------------------------------
    campo_config_adjunto = 'x_adjunto_field_id' # AJUSTAR si aplica
    # campo_adjunto = 'x_auxiliar_file'  # fallback
    campo_adjunto = record.x_adjunto_field_id.name # fallback


    if campo_config_adjunto in record._fields:
        config = record[campo_config_adjunto]
        if config and config.name:
            campo_adjunto = config.name

# -------------------------------------------------
# Campo fecha dinámico
# -------------------------------------------------
    campo_fecha = False
    if record.x_date_field_id and record.x_date_field_id.name:
        campo_fecha = record.x_date_field_id.name

# -------------------------------------------------
# 2) Construcción del dominio
# -------------------------------------------------
    try:
        f = self.env['ir.filters'].new({
            'domain': record.domain or '[]',
            'model_id': model_id,
            'user_id': self.env.user.id,
        })
        dom = f._get_eval_domain()
        dom = list(dom) if isinstance(dom, (list, tuple)) else []
    except Exception:
        dom = []

# Forzar existencia del archivo
    dom.append((campo_adjunto, '!=', False))

# -------------------------------------------------
# 3) Orden dinámico
# -------------------------------------------------
    ordenar = 'id desc'

    if campo_fecha and campo_fecha in TargetModel._fields:
        ordenar = (
            campo_fecha + ' desc, id desc'
                if not record.x_order
                else campo_fecha + ' asc, id asc'
        )
    else:
        if 'write_date' in TargetModel._fields:
            ordenar = 'write_date desc, id desc' if record.x_order else 'write_date asc, id asc'
        elif 'create_date' in TargetModel._fields:
            ordenar = 'create_date desc, id desc' if record.x_order else 'create_date asc, id asc'
        else: ordenar = 'id desc' if record.x_order else 'id asc'

    # -------------------------------------------------
    # 4) Buscar registros
    # -------------------------------------------------
    records = TargetModel.search(dom, limit=50, order=ordenar)

    # -------------------------------------------------
    # 5) Construcción de líneas
    # -------------------------------------------------
    base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')

    for record2 in records:
        x_attachment_id = False
        x_fecha_val = False
        x_document_url = False

        adj = record2[campo_adjunto]
        # Si es many2one -> recordset con .id
        if adj:
            try:
                x_attachment_id = adj.id

                if adj.website_url:
                    x_document_url = base_url + adj.website_url
            except Exception:
                x_attachment_id = False
                x_document_url = False

        x_fecha_val = False

        # -----------------------------
        # Resolver fecha
        # -----------------------------
        if campo_fecha and campo_fecha in record2._fields:
            field_fecha = record2._fields[campo_fecha]
            tipo = field_fecha.type

            if tipo in ('date', 'datetime'):
                x_fecha_val = record2[campo_fecha]

            elif tipo == 'many2one':
                rel = record2[campo_fecha]
                if rel and 'valid_from' in rel._fields:
                    x_fecha_val = rel['valid_from']

        # -----------------------------
        # Línea One2many
        # -----------------------------
        BiEmple = {
            'x_model_id': model_id,
            'x_attachment_id': x_attachment_id,
            'x_trd_id': record.id,
            'x_fecha_referencia': x_fecha_val,
            'x_document_url': x_document_url,
        }

        lineasBiEmple.append((0, 0, BiEmple))

    # -------------------------------------------------
    # 6) Asignación final (compute correcto)
    # -------------------------------------------------
    record['x_documentos_ids'] = [(5, 0, 0)] + lineasBiEmple