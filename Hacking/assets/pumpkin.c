#include <avr/io.h>
#include <util/delay.h>
 
#define BLINK_DELAY 250

void blink_loading(void);

void blink_a(void);
void blink_e(void);
void blink_h(void);
void blink_i(void);
void blink_o(void);
void blink_p(void);
void blink_q(void);
void blink_r(void);
void blink_s(void);
void blink_u(void);

int main (void)
{
  DDRC |= (1<<DDC0) | (1<<DDC1) | (1<<DDC2);
  DDRC |= (1<<DDC3) | (1<<DDC4) | (1<<DDC5);

  DDRD |= (1<<DDD0);
 
 while(1)
   {
     blink_loading();
     _delay_ms(BLINK_DELAY);

     blink_s();
     _delay_ms(BLINK_DELAY);
     blink_q();
     _delay_ms(BLINK_DELAY);
     blink_u();
     _delay_ms(BLINK_DELAY);
     blink_a();
     _delay_ms(BLINK_DELAY);
     blink_s();
     _delay_ms(BLINK_DELAY);
     blink_h();

     _delay_ms(BLINK_DELAY*4);

     blink_e();
     _delay_ms(BLINK_DELAY);
     blink_r();
     _delay_ms(BLINK_DELAY);
     blink_r();
     _delay_ms(BLINK_DELAY);
     blink_o();
     _delay_ms(BLINK_DELAY);
     blink_r();
     _delay_ms(BLINK_DELAY*4);
   }
}

void blink_loading()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  PORTC |= (1<<PC0);
  _delay_ms(BLINK_DELAY);
  
  PORTC |= (1<<PC1);
  _delay_ms(BLINK_DELAY);

  PORTD |= (1<<PD0);
  PORTC &= ~(1<<PC0);
  _delay_ms(BLINK_DELAY);

  PORTC |= (1<<PC4);
  PORTC &= ~(1<<PC1);
  _delay_ms(BLINK_DELAY);

  PORTC |= (1<<PC3);
  PORTD &= ~(1<<PD0);
  _delay_ms(BLINK_DELAY);

  PORTC |= (1<<PC2);
  PORTC &= ~(1<<PC4);
  _delay_ms(BLINK_DELAY);

  PORTD |= (1<<PD0);
  PORTC &= ~(1<<PC3);
  _delay_ms(BLINK_DELAY);

  PORTC |= (1<<PC5);
  PORTC &= ~(1<<PC2);
  _delay_ms(BLINK_DELAY);

  PORTC |= (1<<PC0);
  PORTD &= ~(1<<PD0);
  _delay_ms(BLINK_DELAY);

  PORTC &= ~(1<<PC5);
  _delay_ms(BLINK_DELAY);

  PORTC &= ~(1<<PC0);
  _delay_ms(BLINK_DELAY);

  /* Keep lights on for BLINK_DELAY */
  

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_a()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights A, B, C, E, F and G */
  PORTC |= (1<<PC0) | (1<<PC1) | (1<<PC2);
  PORTC |= (1<<PC4) | (1<<PC5);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_e()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights A, D, E, F and G */
  PORTC |= (1<<PC0) | (1<<PC3);
  PORTC |= (1<<PC4) | (1<<PC5);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_h()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights B, C, E, F, and G */
  PORTC |= (1<<PC1) | (1<<PC2);
  PORTC |= (1<<PC4) | (1<<PC5);
  
  PORTD |= (1<<PD0);
  
  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_i()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights B and C */
  PORTC |= (1<<PC1) | (1<<PC2);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_o()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights C, D, E, and G */
  PORTC |= (1<<PC2) | (1<<PC3) | (1<<PC4);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_p()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights A, B, E, F, and G */
  PORTC |= (1<<PC0) | (1<<PC1);
  PORTC |= (1<<PC4) | (1<<PC5);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_q()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights A, B, C, F, and G */
  PORTC |= (1<<PC0) | (1<<PC1);
  PORTC |= (1<<PC2) | (1<<PC5);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_r()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights E and G */
  PORTC |= (1<<PC4);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_s()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights A, C, D, F, and G */
  PORTC |= (1<<PC0) | (1<<PC2);
  PORTC |= (1<<PC3) | (1<<PC5);

  PORTD |= (1<<PD0);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}

void blink_u()
{
  /* Set all lights off */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);

  /* Turn on lights B, C, D, E, and F */
  PORTC |= (1<<PC1) | (1<<PC2);
  PORTC |= (1<<PC3) | (1<<PC4) | (1<<PC5);

  /* Keep lights on for BLINK_DELAY */
  _delay_ms(BLINK_DELAY);

  /* Set all lights off again */
  PORTC &= ~((1<<PC0) | (1<<PC1) | (1<<PC2));
  PORTC &= ~((1<<PC3) | (1<<PC4) | (1<<PC5));

  PORTD &= ~(1<<PD0);
}
