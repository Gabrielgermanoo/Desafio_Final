import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ContratosRoutingModule } from './contratos-routing.module';
import { IndexComponent } from './components/index/index.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    IndexComponent,
  ],
  imports: [
    CommonModule,
    ContratosRoutingModule,
    ReactiveFormsModule
  ]
})
export class ContratosModule { }
