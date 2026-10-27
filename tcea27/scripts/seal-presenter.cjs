#!/usr/bin/env node
// Inputs stay outside the public repository. No password or plaintext is logged.
// node seal-presenter.cjs <private HTML> <password file> <public output>
const fs=require('node:fs');const crypto=require('node:crypto');const path=require('node:path');
const [source,passwordFile,output]=process.argv.slice(2);if(!source||!passwordFile||!output)throw Error('Supply a private HTML input, private password file, and public output.');
const project=path.resolve(__dirname,'..'),publicRoot=path.resolve(project,'..');for(const input of [source,passwordFile])if(path.resolve(input).startsWith(publicRoot+path.sep))throw Error('Keep private inputs outside the public repository.');
const password=fs.readFileSync(passwordFile,'utf8').replace(/\r?\n$/,'');if(!password)throw Error('Empty password.');
const salt=crypto.randomBytes(16),iv=crypto.randomBytes(12),iterations=600000,context='MG Learn protected presenter resources v1';
const key=crypto.pbkdf2Sync(password,salt,iterations,32,'sha256'),cipher=crypto.createCipheriv('aes-256-gcm',key,iv);cipher.setAAD(Buffer.from(context));const ciphertext=Buffer.concat([cipher.update(fs.readFileSync(source)),cipher.final(),cipher.getAuthTag()]);key.fill(0);
const payload={version:1,algorithm:'AES-256-GCM',kdf:'PBKDF2-SHA256',iterations,context,salt:salt.toString('base64'),iv:iv.toString('base64'),ciphertext:ciphertext.toString('base64')};
const template=fs.readFileSync(path.join(project,'assets/protected/vault-template.tpl'),'utf8');const html=template.replace('__PAYLOAD__',JSON.stringify(payload));fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,html);console.log('Wrote encrypted presenter resource:',output);
