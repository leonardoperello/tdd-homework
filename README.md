# Trabajo Practico Obligatorio: Test Driven Development (TDD)
<style>
code {
  font-family: Consolas,"courier new";
  color: #f1f1f1;
  background-color: #000000;
  padding: 2px;
  font-size: 105%;
}
</style>


## Instrucciones para correr el proyecto.

En este caso se está utilizando Pytest por lo que para probar los casos de test
es necesario instalarlo en caso de no tenerlo ya, con el siguiente comando:

```bash
 pip install -U pytest
```

Luego para verificar que se instaló correctamente ejecutar

```bash
pytest --version
```

Para correr el programa se hace de la siguiente manera:

```bash
pytest test1.py
```
o para una ejecución mas detallada:
```bash
pytest -q test1.py 
```
 

## Ejemplo de un ciclo de TDD (Red/Green/Refactor) para alguna de las funciones implementadas
.
Una de las funciones implementadas que cumplían con el ciclo de TDD fue la siguiente
```python
def testStrike():
      g=Game([])
      g.roll(10)
      assert g.strike(0)

```
En la siguiente imágen se muestra el error en el código por el cual no pasó el test
![REDStrike-TDD](Screenshots/red%20strike%202.png)

```  
En este caso, nos encontramos en la primer fase del ciclo ya que al ejecutar este test, obtuvimos un error.  
En la siguiente imágen se muestra el error en el código por el cual no pasó el test  

![REDStrike-TDD]Screenshots/red%20strike2.png  

Esto se debió a que en la función roll se pedían dos parametros pero se le dió uno solo.
Dado que el error en el código se presentaba en la funcionalidad roll, lo corregimos de esta forma:

```python
def roll(self):
        self.rolls.append(pins)
        
        
def strike():
      if(self.rolls[roll_])==10):
            return True
```
Luego vimos que éste código se podía mejorar por lo que le hicimos el siguiente refactor:

```python
def strike():
      return (self.rolls[roll_]==10)
```
A su vez, verificamos que este refactor pasara el test:
![RefactorStrike-TDD](Screenshots/refactor%20strike.png)
.
.
.
.
.
## Tipos de Test aplicados y ejemplos (remitirse a la teoría de la materia).
.
.
.
.
.
.
.
## Conclusiones:
### Dificultades y ventajas percibidas en cuanto a la metodología TDD y al proyecto en sí, críticas constructivas
<ul>
  <p>A la hora de realizar este trabajo se hizo uso de Github para poder tener un mejor control de versiones a medida que íbamos programando. Esto fue un desafío para nosotros ya que estábamos más acostumbrados a usar entornos como Gitkraken por lo que a la hora de usar los comandos en la terminal pudimos ver un cambio. Además, pudimos ver cómo crear ramas hacía el trabajo más ordenado ya que ninguno de los dos estaba acostumbrado a hacer esto. En cuanto a las dificultades presentadas con esta metodología, se tuvo un par de problemas a la hora de hacer los pull request que hicimos rápidamente y sin observar que se los realizamos a la rama del profesor.</p>  
  <p>Por otro lado, como adoptamos la metodología de pair programming (mediante videollamadas compartiendo pantalla), pudimos aprovechar los conocimientos de cada uno sobre un lenguaje en el cual ninguno tiene mucha experiencia y fuimos llevando a cabo ciclos de TDD.  En cuanto a la metodología TDD, no encontramos dificultades e incluso consideramos que fue muy útil en nuestro caso dados nuestros conocimientos sobre el lenguaje.</p>
