#!/usr/bin/env python
"""
Created on @ 2020
@author: 
"""
#imports
from flask import Flask, render_template, json, request, session, redirect
import os
import sys
import time
from flaskext.mysql import MySQL


#initialize the flask and SQL Objects
app = Flask(__name__)
mysql = MySQL()

#configure MYSQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Guavus@123'
app.config['MYSQL_DATABASE_DB'] = 'op_dashboard_new'
app.config['MYSQL_DATABASE_HOST'] = '192.168.133.196'
#app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

#define methods for routes (what to do and display)
@app.route('/')
def home():
    return 'Hello Operation Dashboard!'

@app.route('/clusters')
def clusters():
    try:
        print("Showing Clusters!!")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cluster_info")
        data = cursor.fetchall()
        return render_template("clusters.html", value=data)
    except Exception as e:
        return render_template("cluster_fresh.html", error = str(e))

@app.route('/add_cluster', methods = ['GET', 'POST'])
def add_cluster():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['description']:
         return('Please enter cluster name the fields', 'error')
        else:
            new_cluster_name=request.form['email']
            cluster_description=request.form['description']
            cluster_date=time.strftime('%Y-%m-%d %H:%M:%S')
            conn = mysql.get_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO cluster_info(cluster_name, cluster_desc, cluster_creation_date) VALUES (%s,%s,%s)", (new_cluster_name,cluster_description,cluster_date))
            conn.commit()
 #           return('Cluster was successfully added!!!')
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT cluster_name FROM cluster_info WHERE cluster_name = %s LIMIT 1", (new_cluster_name))
            data1 = cursor.fetchone()
            data2 = data1[0]
            if data2 == request.form['email']:
                new_cluster_name=request.form['email']
                host_group1=request.form['hg1']
                ip_address1=request.form['ip1']
                fqdn1=request.form['fq1']
                host_group2=request.form['hg2']
                ip_address2=request.form['ip2']
                fqdn2=request.form['fq2']
                host_group3=request.form['hg3']
                ip_address3=request.form['ip3']
                fqdn3=request.form['fq3']
                host_group4=request.form['hg4']
                ip_address4=request.form['ip4']
                fqdn4=request.form['fq4']
                host_group5=request.form['hg5']
                ip_address5=request.form['ip5']
                fqdn5=request.form['fq5']
                host_group6=request.form['hg6']
                ip_address6=request.form['ip6']
                fqdn6=request.form['fq6']
                host_group7=request.form['hg7']
                ip_address7=request.form['ip7']
                fqdn7=request.form['fq7']
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT cluster_id FROM cluster_info where cluster_name = %s LIMIT 1", (new_cluster_name))
                clust_id_temp = cursor.fetchone()
                clust_id = clust_id_temp[0]
                suffix = "_host_info"
 #              table_name = new_cluster_name + suffix
 #              return table_name
                conn1 = mysql.get_db()
                cur = conn1.cursor()
                cur.execute("CREATE TABLE `%s`(cluster_id INT NOT NULL, cluster_name VARCHAR(20) NOT NULL, host_id INT NOT NULL AUTO_INCREMENT, hostgroup VARCHAR(20) NOT NULL, host_IP VARCHAR(20) NOT NULL,host_fqdn VARCHAR(200) NOT NULL,host_live VARCHAR(20), PRIMARY KEY (host_id))", (new_cluster_name))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group1, ip_address1, fqdn1))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group2, ip_address2, fqdn2))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group3, ip_address3, fqdn3))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group4, ip_address4, fqdn4))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group5, ip_address5, fqdn5))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group6, ip_address6, fqdn6))
                cur.execute("INSERT INTO `%s`(cluster_id, cluster_name, hostgroup, host_IP, host_fqdn) VALUES (%s, %s, %s, %s, %s)", (new_cluster_name, clust_id, new_cluster_name, host_group7, ip_address7, fqdn7))
                conn1.commit()
                conn1.close()
                return('Host Detail was successfully added')
            else:
                return('Cluster with that name not exist!!')
    return render_template('addcluster.html')


@app.route('/hosts/<cluster_name>')
def hosts(cluster_name):
    try:
        print("Showing Host List!!")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT hostgroup, host_IP, host_fqdn, host_live FROM %s", (cluster_name))
        data = cursor.fetchall()
        return render_template("hosts.html", value=data)
    except Exception as e:
        return render_template("hosts_fresh.html", error = str(e))
"""

@app.route('/checklist/<cluster-name>')
def checklist():
    try:
        os.system("sh test.sh")
        os.system("sh test.sh")
        print("Running Check List!!")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM host_<clsuter-name>")
        data = cursor.fetchall()
        return render_template("Checklist.html", value=data)
    except Exception as e:
        return render_template("hosts_fresh.html", error = str(e))
"""

if __name__ == "__main__":
    app.run()