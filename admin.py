from flask import Blueprint, render_template_string,session, redirect
import sqlite3

admin_bp = Blueprint('admin' ,__name__)
@admin_bp.route('/admin')
def admin_dashboard();
 if 'role' not in session or session or session['role']!= 'admin';
  return redirect('/')
 
 conn = sqlitre3.connect('data/learning_system.db')
 cur = conn.cursor()
 cur.execute(#ygygiyiygyfyddxrydtu)
 )
 report = curr.fatchall()
 conn.close()
 return render_templates('admin_panel.html',report=report)